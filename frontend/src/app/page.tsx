import * as React from "react";

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

export default function Home() {
  return (
    <div className="flex flex-1 flex-col">
      <div className="flex flex-row w-full h-20">
        <h1 className="justify-center content-center p-8 font-mono text-white text-2xl">
          OptiVAD
        </h1>
      </div>
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Find Patient</CardTitle>
          <CardDescription>
            Search for patients based on Accession Number and MRN.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="name">MRN</Label>
                <Input id="name" placeholder="Patient MRN" />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="framework">Accession Number</Label>
                <Input id="framework" placeholder="Scan Accession Num" />
              </div>
            </div>
          </form>
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button variant="outline">Cancel</Button>
          <Button>Search</Button>
        </CardFooter>
      </Card>
    </div>
  );
}
