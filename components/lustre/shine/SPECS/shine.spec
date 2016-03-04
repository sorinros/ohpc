%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %define PROJ_DELIM -ohpc}

# Base package name
%define pname shine

Name:      %{pname}%{PROJ_DELIM}
Summary:   Lustre administration utility
Version:   1.4
Release:   1%{?dist}
Source0:   https://github.com/cea-hpc/%{pname}/archive/v%{version}.tar.gz
License:   GPLv2
Group:     Applications/System
Vendor:    CEA
Url:       http://lustre-shine.sourceforge.net/
DocDir:         %{OHPC_PUB}/doc/contrib
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python
#!BuildIgnore: post-build-checks
Requires:  clustershell%{PROJ_DELIM} >= 1.5.1
Provides:  %{pname} = %{version}

# Default library install path
%define install_path %{OHPC_LIBS}/%{pname}/%version

%description
Lustre administration utility.

%prep
%setup -q -n %{pname}-%{version}

%build
export SHINEVERSION=%{version}
python setup.py build

%install
export SHINEVERSION=%{version}
#python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
python setup.py install --root=%{buildroot} --prefix="%{install_path} --record=INSTALLED_FILES
mkdir -p %{buildroot}%{install_path}/%{_sysconfdir}/shine/models
cp conf/*.conf* %{buildroot}%{install_path}/%{_sysconfdir}/shine
cp conf/models/* %{buildroot}%{install_path}/%{_sysconfdir}/shine/models
# man pages
mkdir -p %{buildroot}%{install_path}/%{_mandir}/{man1,man5}
gzip -c doc/shine.1 >%{buildroot}%{install_path}/%{_mandir}/man1/shine.1.gz
gzip -c doc/shine.conf.5 >%{buildroot}%{install_path}/%{_mandir}/man5/shine.conf.5.gz

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE README ChangeLog
%{OHPC_HOME}
%{OHPC_PUB}

%changelog
* Wed Feb 24 2016 <aurelien.degremont@cea.fr> - 1.4-1
- Initial packaging for OpenHPC
