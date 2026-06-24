# Project Ideas and Research Notes

---
## Attempts during the project
### Setup and Configuration
- Link my local repository to the remote repository on GitHub.
  - `Failed` Cannot push because of **authentication issues**.
  - `Solution` Generate a new **SSH key** and add it to the GitHub account.
- Push my local repository to the remote repository on GitHub.
  - `Failed` Repository histories **diverged**.
  - `Solution` Use `git pull --rebase` to **synchronise** the local repository with the remote repository.
- Copy the project files to the Raspberry Pi 5.
  - `Failed` The Raspberry Pi 5 **cannot connect** to the account.
  - `Solution` Apply **SSH key** to authenticate the Raspberry Pi 5.
### Vision thresholding
- Implement RGB selection algorithm to detect red objects.
  - `Failed` The algorithm **misses** some red objects.
  - `Solution` Implement relative RGB values `R > 80, R > G * 1.3, R > B * 1.3` to detect red objects.