"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { formatDistance, subSeconds } from "date-fns";
import { AnimatePresence, motion } from "framer-motion";
import React, { useEffect } from "react";
import { useRef, useState } from "react";
import { RefreshCw } from "lucide-react";

type Message =
  | {
      type: "text";
      message: string;
      timestamp: Date;
    }
  | {
      type: "choice";
      message: { prompt: string; id: number }[];
      disabled: boolean;
      timestamp: Date;
    };

export function Main() {
  // history
  const [history, setHistory] = useState<Message[]>([
    {
      type: "text",
      message:
        "hi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smh",
      timestamp: subSeconds(new Date(), 3),
    },
    {
      type: "choice",
      message: [
        { prompt: "yes", id: 1 },
        { prompt: "no", id: 2 },
        { prompt: "HUGGGEEE PROMPT", id: 3 },
        { prompt: ".............................", id: 4 },
      ],
      disabled: true,
      timestamp: subSeconds(new Date(), 2),
    },
  ]);

  // websocket to server
  const url = "ws://localhost:8000/ws";
  useEffect(() => {
    const ws = new WebSocket(url);

    // open
    ws.addEventListener("open", () => {
      console.log("connected to server");
    });

    // close
    ws.addEventListener("close", () => {
      console.log("disconnected from server");
    });

    // message
    ws.addEventListener("message", (event) => {
      console.log("received: ", event.data);
    });
  });

  // (auto) scroll to bottom
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
      <h1 className="text-4xl font-extrabold tracking-tight text-white sm:text-[5rem]">
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
                  <span
                    className={cn(
                      "flex max-w-xs flex-col rounded-md bg-gray-700 bg-opacity-75 p-3",
                      message.type === "text" ? "-space-y-1" : "space-y-3",
                    )}
                  >
                    {message.type === "text" ? (
                      <span className="text-sm text-background">
                        {message.message}
                      </span>
                    ) : (
                      <div
                        className={cn(
                          "align-center grid h-fit items-center",
                          // "space-y-2",
                          // "space-x-4",
                          "gap-4 auto-rows-auto",
                        )}
                      >
                        {message.message.map((choice) => (
                            <Button
                              key={choice.id}
                              variant="outline"
                              className="bg-gray-700 h-[70px]"
                              onClick={() => {
                                setHistory([
                                  ...history,
                                  {
                                    type: "text",
                                    message: `You chose ${choice.prompt}`,
                                    timestamp: new Date(),
                                  },
                                ]);
                                // websocket.send()
                              }}
                            >
                              {choice.prompt}
                            </Button>
                        ))}
                        <span
                          onClick={() =>
                            setHistory([
                              ...history,
                              {
                                type: "text",
                                message: "Refreshing agent options...",
                                timestamp: new Date(),
                              },
                            ])
                          }
                        >
                          <RefreshCw className="h-[70px] w-[70px] rounded-sm border bg-gray-700 p-2" />
                        </span>
                      </div>
                    )}
                    <span className="align-self-bottom h-full text-end text-xs italic text-background/50">
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
    </div>
  );
}
