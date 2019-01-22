Name:           vi-vim-link
Version:        0.0.1
Release:        1%{?dist}
Summary:        Provides /usr/bin/vi from /usr/bin/vim (vim-enhanced)

License:        MIT

BuildArch:      noarch

BuildRequires:  vim-enhanced,coreutils
Requires:       vim-enhanced
Conflicts:      vim-minimal
Provides:       /usr/bin/vi

%description
Creates a symbolic link at /usr/bin/vi to satisfy requirements for visudo
in environments where vim-enhanced is installed without vim-minimal


%prep


%build


%install
[ -d "%{buildroot}" ] && %{__rm} -rf %{buildroot}
[ -d "%{buildroot}" ] || %{__mkdir} -p %{buildroot}/usr/bin
ln -sf /usr/bin/vim %{buildroot}/usr/bin/vi


%files
/usr/bin/vi

%changelog
* Tue Jan 22 2019 JimBobMcGee - 0.0.1
- Initial creation
