import { z } from "zod";

export const patientSchema = z.object({
  patient_id: z.string(),
  study_id: z.string(),
});

export type patient = z.infer<typeof patientSchema>;
