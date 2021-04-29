# bash-completion-for-doas

## Introduction

Please review my patches, **https://github.com/nutta-git/bash-completion-for-doas/blob/master/completions/doas**

before using this code base. I only replaced the word sudo with doas. I don't know the security implications of this procedure. With that being said, 
## Use this source code at your own risk! 

**https://github.com/nutta-git/bash-completion-for-doas/blob/master/completions/doas**

bash-completion-for-doas is a collection of command line command completions for the
[Bash shell](https://www.gnu.org/software/bash/), collection of helper
functions to assist in creating new completions, and set of facilities for
loading completions automatically on demand, as well as installing them.

## Installation

### Arch Linux

```shell
git clone https://github.com/nutta-git/bash-completion-for-doas
cd bash-completion-for-doas
makepkg -si 
```

