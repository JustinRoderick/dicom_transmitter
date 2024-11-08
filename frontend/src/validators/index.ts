import { z } from "zod";

// Schema for patient
// !! Might need to seperate the patient_id and study_id
export const PatientRequestSchema = z.object({
  patient_id: z.string(),
  study_id: z.string(),
});

export type patientRequest = z.infer<typeof PatientRequestSchema>;

export const PatientResponseSchema = z.object({
  message: z.string(),
  data: z.any(),
});

export type patientResponse = z.infer<typeof PatientResponseSchema>;
