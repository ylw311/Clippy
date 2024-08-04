#!/bin/bash

# Start a new tmux session and detach from it
tmux new-session -d -s devSession

# Split the window into two panes horizontally
tmux split-window -h

# Select the first pane (0) and run the first command
tmux send-keys -t 0 'source env/bin/activate' Enter
tmux send-keys -t 0 'cd ui' Enter
tmux send-keys -t 0 'bun dev' Enter

# Select the second pane (1) and run the second command
tmux send-keys -t 1 'source env/bin/activate' Enter
tmux send-keys -t 1 'python main.py' Enter

# Attach to the tmux session
tmux attach-session -t devSession
