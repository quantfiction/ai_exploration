# AI Coding Assistant Benchmark

## Introduction

This document provides a quantitative comparison of DeepSeek-powered coding assistants: Aider, Cline, and Cursor. Each tool was evaluated based on an identical coding task. The metrics used for comparison include completion time, code quality, interaction efficiency, time-to-first-working-solution, and the number of interaction rounds needed.

## Task Descriptions

1. **Task 1: Email Handler
   - Objective: Develop a system in python that converts convictions in positions into units of risk in a portfolio and then converts that into position sizes
   - Requirements: Takes sensible steps for converting convictions and risk and converts them into positions

## Metrics

- **Completion Time**: Total time taken to complete the task.
- **Code Quality**: Evaluation of the code based on readability, maintainability, and adherence to best practices.
- **Interaction Efficiency**: Number of interactions required to reach a solution.
- **Time-to-First-Working-Solution**: Time taken to reach the first working version of the solution.
- **Number of Interaction Rounds**: Total number of back-and-forth interactions needed.

## Results

### Task 1

| Metric                        | Aider | Cline | Cursor |
|-------------------------------|-------|-------|--------|
| Completion Time               |25 min |20 min |< 5 min |
| Code Quality                  |Good   |Good   |Poor    |
| Interaction Efficiency        |Fair   |Good   |Poor    |
| Time-to-First-Working-Solution|20 min |5 min |30s      |
| Number of Interaction Rounds  |6      |3      |5       |


## Conclusion

Cursor either isn't set up properly or isn't as capable as the other tools. Aider seems very capable, but the CLI workflow isn't necessarily for me. Cline seems like the best fit for me at this time.
