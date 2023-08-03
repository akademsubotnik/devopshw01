Name:           devopshw01
Version:        1.0.0
Release:        1%{?dist}
Summary:        Hello World example implemented in python

License:        GPLv3+
URL:            https://github.com/akademsubotnik/%{name}
Source0:        https://github.com/akademsubotnik/devopshw01/releases/download/1.0.0/devopshw01-1.0.0.tar.gz

BuildRequires:  python
Requires:       python
Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in
Python.

%prep
%setup -q

%build

python -m compileall %{name}.py

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/

%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.1.1-1
  - First pello package
