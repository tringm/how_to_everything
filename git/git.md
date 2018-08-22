# Git

## Fetch

Fetch new info from git. Doesn't merge

## Merging issues
1. Rebase:

```
git pull --rebase
```
Doesn't merge. Add conflict on top of head instead of merge

```
git rebase --abort
```

2. Stash:

```
git stash
```

Stash staged content (after add)

3. Reverting:

```
Reset staged
git add => git reset
```

```
Reset commit but keep file
git commit => git reset => git Head~<no_of_behind_HEAD> (git Head~1)
git reset HEAD^

```
