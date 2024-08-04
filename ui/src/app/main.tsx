"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { formatDistance, subSeconds } from "date-fns";
import { AnimatePresence, motion } from "framer-motion";
import React, { useEffect } from "react";
import { useRef, useState } from "react";
import { RefreshCw } from "lucide-react";
import useWebSocket, { ReadyState } from "react-use-websocket";

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
    // {
    //   type: "text",
    //   message:
    //     "hi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smhhi.. lorem ipsum bruh smh",
    //   timestamp: subSeconds(new Date(), 3),
    // },
    // {
    //   type: "choice",
    //   message: [
    //     { prompt: "yes", id: 1 },
    //     { prompt: "no", id: 2 },
    //     { prompt: "HUGGGEEE PROMPT", id: 3 },
    //     { prompt: ".............................", id: 4 },
    //   ],
    //   disabled: true,
    //   timestamp: subSeconds(new Date(), 2),
    // },
  ]);

  // websocket to server
  const url = "ws://127.0.0.1:8000/ws";

  const { sendJsonMessage, lastJsonMessage, readyState, getWebSocket } = useWebSocket(url, {
    share: false,
    shouldReconnect: () => true,
  });

  useEffect(() => {
    console.log("Connection state changed");
    if (readyState === ReadyState.OPEN) {
      console.log("Connected to server");
    }
  }, [readyState]);

  // useEffect(() => {
  //   getWebSocket()?.addEventListener("message", (event) => {
  //     console.log("Received a new message", event);
  //     // const newMsg = JSON.parse(event.data) as Message;
  //     // setHistory([...history, newMsg]);
  //   })
  // }, []);

  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
    if(!lastJsonMessage) return
    console.log(`Got a new message: ${lastJsonMessage}`);
    const newMsg = JSON.parse(lastJsonMessage as string) as Message;
    console.log(newMsg);
    setHistory([...history, newMsg]);
  }, [lastJsonMessage]);

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
      <h1 className="grid text-center font-extrabold tracking-tight text-white">
        <span className="text-[3rem] text-[hsl(280,100%,70%)]">Clippy ✂️</span>
        <span className="text-2xl text-white">Dashboard</span>
      </h1>

      {/* EVENT LOG */}
      {/* <h2 className="text-3xl font-bold sm:text-[2rem]">Event Log</h2> */}
      <div className="flex h-full w-full flex-col overflow-y-auto overflow-x-hidden rounded-sm border">
        <div
          ref={messagesContainerRef}
          className="flex h-full w-full flex-col overflow-y-auto overflow-x-hidden"
        >
          <AnimatePresence>
            {history?.length === 0 && (
              <div className="flex size-full items-center bg-gray-800 p-12 text-center align-middle text-xl font-bold italic text-muted">
                Stop using your clipboard to start using Clippy! 📋
              </div>
            )}
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
                          "auto-rows-max gap-4",
                        )}
                      >
                        {message.message.map((choice) => (
                          <Button
                            key={choice.id}
                            variant="outline"
                            className="h-[70px] bg-gray-700"
                            onClick={() => {
                              setHistory([
                                ...history,
                                {
                                  type: "text",
                                  message: `You chose ${choice.prompt}`,
                                  timestamp: new Date(),
                                },
                              ]);
                              sendJsonMessage({
                                event: "subscribe",
                                data: {
                                  channel: "general-chatroom",
                                },
                              });
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
