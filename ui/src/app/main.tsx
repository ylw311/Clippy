"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { formatDistance, subSeconds } from "date-fns";
import { AnimatePresence, motion } from "framer-motion";
import React from "react";
import { useRef, useState } from "react";

export function Main() {
  const [history, setHistory] = useState<
    {
      message: string;
      timestamp: Date;
    }[]
  >([
    {
      message:
        "hi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smh",
      timestamp: subSeconds(new Date(), 3),
    },
  ]);

  // scroll to bottom

  const messagesContainerRef = useRef<HTMLDivElement>(null);

  React.useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [history]);

  return (
    <div className="overflow-y-none mx-auto flex h-dvh max-w-3xl flex-col items-center justify-center space-y-4 px-8 py-4 text-white">
      {/* PROJECT NAME */}
      <h1 className="text-5xl font-extrabold tracking-tight text-white sm:text-[5rem]">
        <span className="text-[hsl(280,100%,70%)]">Clippy ✂️</span>
      </h1>

      {/* EVENT LOG */}
      {/* <h2 className="text-3xl font-bold sm:text-[2rem]">Event Log</h2> */}
      <div className="flex h-full w-full flex-col overflow-y-auto overflow-x-hidden rounded-sm border">
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
                  <span className="flex max-w-xs flex-col -space-y-1 rounded-md bg-gray-700 bg-opacity-75 p-3">
                    <span className="text-background text-sm">
                      {message.message}
                    </span>
                    <span className="text-background/50 align-self-bottom h-full text-end text-xs italic">
                      {formatDistance(message.timestamp, new Date(), {
                        addSuffix: true,
                        includeSeconds: true,
                      })}
                    </span>
                  </span>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      </div>
      <Button
        onClick={() =>
          setHistory([
            ...history,
            {
              message: "hi",
              timestamp: new Date(),
            },
          ])
        }
        className="w-full"
        variant="default"
      >
        Add message
      </Button>
    </div>
  );
}
