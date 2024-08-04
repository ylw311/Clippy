"use client";

import { cn } from "@/lib/utils";
import { AnimatePresence, motion } from "framer-motion";
import React from "react";
import { useRef, useState } from "react";

export function Main() {
  const [history, setHistory] = useState<
    {
      message: string;
      timestamp: string;
    }[]
  >([{
    message: "hi",
    timestamp: "now",
  }]);

  // scroll to bottom

  const messagesContainerRef = useRef<HTMLDivElement>(null);

  React.useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [history]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center space-y-4 bg-slate-900 px-8 py-4 text-white">
      {/* PROJECT NAME */}
      <h1 className="text-5xl font-extrabold tracking-tight text-white sm:text-[5rem]">
        <span className="text-[hsl(280,100%,70%)]">Clippy</span>
      </h1>

      {/* EVENT LOG */}
      <h2 className="text-3xl font-bold sm:text-[2rem]">Event Log</h2>
      <div className="w-full flex-auto rounded-sm border">
        <div
          ref={messagesContainerRef}
          className="flex h-full w-full flex-col overflow-y-auto overflow-x-hidden"
        >
          <AnimatePresence>
            {history?.map((message, index) => (
              <motion.div
                key={index}
                layout
                initial={{ opacity: 0, scale: 1, y: 50, x: 0 }}
                animate={{ opacity: 1, scale: 1, y: 0, x: 0 }}
                exit={{ opacity: 0, scale: 1, y: 1, x: 0 }}
                transition={{
                  opacity: { duration: 0.1 },
                  layout: {
                    type: "spring",
                    bounce: 0.3,
                    duration: history.indexOf(message) * 0.05 + 0.2,
                  },
                }}
                style={{
                  originX: 0.5,
                  originY: 0.5,
                }}
                className={cn(
                  "flex flex-col gap-2 whitespace-pre-wrap p-4",
                  "items-end",
                )}
              >
                <div className="flex items-center gap-3">
                  <span className="bg-accent text-foreground max-w-xs rounded-md p-3">
                    {message.message}
                  </span>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      </div>
    </div>
  );
}
