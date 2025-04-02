
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c99 -O2
LDFLAGS = -lm

# Target for the bisection method
BISECTION_SRC = newton.c
BISECTION_OBJ = $(BISECTION_SRC:.c=.o)
BISECTION_BIN = newton

# Default target
all: $(BISECTION_BIN)

# Compile bisection program
$(BISECTION_BIN): $(BISECTION_OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Generate object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean built files
clean:
	rm -f $(BISECTION_BIN) $(BISECTION_OBJ)

# Run the bisection program
run: $(BISECTION_BIN)
	./$(BISECTION_BIN)

.PHONY: all clean run
