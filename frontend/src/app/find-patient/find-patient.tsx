import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { FindPatientAction } from "./find-patient-action";

export function FindPatient() {
  const [patientId, setPatientId] = useState<string>("");
  const [studyId, setStudyId] = useState<string>("");
  const [response, setResponse] = useState<string>("");

  return (
    <div className="flex flex-1 items-center justify-center">
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Find Patient</CardTitle>
          <CardDescription>
            Search for patients based on Accession Number and MRN.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form
            onSubmit={(e) =>
              FindPatientAction(e, patientId, studyId, setResponse)
            }
          >
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label>MRN</Label>
                <Input
                  id="mrn"
                  placeholder="Patient MRN"
                  value={patientId}
                  onChange={(e) => setPatientId(e.target.value)}
                />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label>Accession Number</Label>
                <Input
                  id="accession"
                  placeholder="Scan Accession Num"
                  value={studyId}
                  onChange={(e) => setStudyId(e.target.value)}
                />
              </div>
            </div>
          </form>
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button
            onClick={(e) =>
              FindPatientAction(e, patientId, studyId, setResponse)
            }
          >
            Search
          </Button>
        </CardFooter>
        <div className="p-4">
          <p>{response}</p>
        </div>
      </Card>
    </div>
  );
}
