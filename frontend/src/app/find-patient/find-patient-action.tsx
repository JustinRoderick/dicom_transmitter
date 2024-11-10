import { PatientRequestSchema, PatientResponseSchema } from "@/validators";

export async function FindPatientAction(
  e: React.FormEvent,
  patientId: string,
  studyId: string,
  setResponse: React.Dispatch<React.SetStateAction<string>>
) {
  e.preventDefault();

  const payload = { patient_id: patientId, study_id: studyId };

  const parsedPayload = PatientRequestSchema.safeParse(payload);
  if (!parsedPayload.success) {
    setResponse("Invalid payload");
    return;
  }

  try {
    // Need to find correct route URL
    const response = await fetch("https://localhost:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    const parsedResponse = PatientResponseSchema.safeParse(data);
    if (!parsedResponse.success) {
      setResponse("Invalid response");
      return;
    }

    setResponse(parsedResponse.data.message);
  } catch (error) {
    console.error(error);
    setResponse("Error fetching data");
    return;
  }
}
