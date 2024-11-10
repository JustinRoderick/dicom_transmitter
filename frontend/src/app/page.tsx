import * as React from "react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

export default function Page() {
  return (
    <div className="">
      <div className="flex flex-col w-full h-20">
        <h1 className="justify-center content-center p-8 font-mono text-white text-2xl">
          OptiVAD
        </h1>
      </div>
      <div className="p-4 items-center justify-center">
        <Link href="/find-patient">
          <Button className="m-4 bg-white text-black hover:bg-gray-400">
            Get Started
          </Button>
        </Link>
      </div>
    </div>
  );
}
