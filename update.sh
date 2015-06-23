#!/bin/bash

branch="$1"
old_commit=$(git rev-parse $2)
new_commit=$(git rev-parse $3)

print "Moving $branch from $old_commit to $new_commit"
