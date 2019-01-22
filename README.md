# vi-vim-link
Intended to resolve a package dependency between **sudo** and **vim-minimal** by 'providing' a symlink to `/usr/bin/vim` at `/usr/bin/vi`.

## Purpose
Removing **vim-minimal** (e.g. after installing **vim-enhanced**) will take **sudo** with it, if you are not careful.  You *can* remove **vim-minimal**, but then the package database will complain about the missing dependency.  Since **sudo** only needs `vi` because of `visudo`, and `vim` is a suitable replacement for `vi`, we can `rpm -e --nodeps vim-minimal; ln -s /usr/bin/vim /usr/bin/vi` and still be in a working state.

*However*, the package manager still complains about the missing `/usr/bin/vi`, because the package spec for **sudo** (incorrectly?) requires a *package* called **/usr/bin/vi** and only **vim-minimal** *provides* it.

    root@localhost ~# yum remove vim-minimal
      Loaded plugins: fastestmirror
      Resolving Dependencies
      --> Running transaction check
      ---> Package vim-minimal.x86_64 2:7.4.160-5.el7 will be erased
      --> Processing Dependency: /usr/bin/vi for package: sudo-1.8.23-3.el7.x86_64
      --> Restarting Dependency Resolution with new changes.
      --> Running transaction check
      ---> Package sudo.x86_64 0:1.8.23-3.el7 will be erased
      --> Finished Dependency Resolution
      
      Dependencies Resolved
      ==============================================================================================================
       Package                        Arch                 Version                   Repository                Size
      ==============================================================================================================
      Removing:
       vim-minimal                    x86_64               2:7.4.160-5.el7           @base                    896 k
      Removing for dependencies:
       sudo                           x86_64               1.8.23-3.el7              @base                    3.0 M
       
      Transaction Summary
      ==============================================================================================================
      Remove  1 Package (+1 Dependent package)
       
      Installed size: 3.9 M
      Is this ok [y/N]: n

    root@localhost ~# rpm -e --nodeps vim-minimal
    
    root@localhost ~# yum install vim-enhanced
      Loaded plugins: fastestmirror
      Resolving Dependencies
      --> Running transaction check
      ---> Package vim-enhanced.x86_64 2:7.4.160-5.el7 will be installed
      --> Finished Dependency Resolution

      Dependencies Resolved

      ==============================================================================================================
       Package                         Arch                Version                   Repository                Size
      ==============================================================================================================
      Installing:
       vim-enhanced                          x86_64              2:7.4.160-5.el7           base               1.0 M

      Transaction Summary
      ==============================================================================================================
      Install  1 Package

      Total download size: 1.0 M
      Installed size: 2.2 M
      Is this ok [y/d/N]: y
  
    root@localhost ~# package-cleanup --problems
      Loaded plugins: fastestmirror
      Package sudo-1.8.23-3.el7.x86_64 has missing requires of /usr/bin/vi

## Caveat
This is much a chance for me to learn a bit about RPM packaging as it is to resolve the dependency issue.  Use it at your own risk.  I'll happily take advisement on how to better package the workaround, or even better workarounds, but I'm not supporting this. :-)

I fully-expect this has been fixed properly (by experienced package maintainers) in more-recent RHEL-based distros, but it hasn't made it to CentOS 7 yet, so I've knocked this up.

## Installation 
    rpm -e --nodeps vim-minimal
    yum install "https://raw.githubusercontent.com/jimbobmcgee/vi-vim-link/master/vi-vim-link-0.0.1-1.el7.noarch.rpm"
    package-cleanup --problems
    ls -l /usr/bin/vi*
  
## Uninstall/Reversion
    rpm -e --nodeps vi-vim-link
    yum install vim-minimal
    package-cleanup --problems
    ls -l /usr/bin/vi*
