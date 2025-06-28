#!/bin/bash


# Simulate real status for untracked files by replacing ?? with A
git add .
name_status=$(git diff --name-status develop ) # TODO: Suppress standard output error after develop, inside (git diff --name-status develop )
