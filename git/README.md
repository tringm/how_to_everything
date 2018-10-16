# Git

## Branches

1. List all branches:

```
git branch -a
```

2. Check out to branch:

```
git checkout <branch_name>
```

## Merge

1. Fast-forward merging:

<href>https://confluence.atlassian.com/bitbucket/use-a-git-branch-to-merge-a-file-681902555.html</href>
Merge the fixing branch with faster
* Switch to branch + pull
* Switch to master ```git checkout master```
* Merge ```git merge <branch-name>```
* Resolve conflict if necessary with ```git mergetool``` and continue merge ```git commit``` then ```git push```
* Delete the fixing branch ```git branch -d <branch-name>```
* Check with git status

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

```
# Reset master back to origin/master
git reset --hard origin/master
```

## Checkout
1. Ignore unstaged changes:

```
git checkout -- .
```

For a specific file

```
git checkout path/to/file
```

