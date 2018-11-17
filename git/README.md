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

## Change commit messages


### Not pushed + most recent commit:
```bash
git commit --amend
```

### Already pushed + most recent commit:

```bash
git commit --amend
git push origin master --force
```

**Force pushing your commit after changing prevent others to sync with the repo**

## Not pushed + old commit:
```bash
git rebase -i HEAD~X
# X is the number of commits to go back
# Move to the line of your commit, change pick into edit,
# then change your commit message:
git commit --amend
# Finish the rebase with:
git rebase --continue
```
Rebase opened your history and let you pick what to change. With edit you tell you want to change the message. Git moves you to a new branch to let you --amend the message. git rebase --continue puts you back in your previous branch with the message changed.

## Already pushed + old commit:
Edit your message with the same 3 steps process as above (`rebase -i`, `commit --amend`, `rebase --continue`).
Then force push the commit:
```bash
git push origin master --force
```
