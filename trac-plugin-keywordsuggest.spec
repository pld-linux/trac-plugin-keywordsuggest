%define		trac_ver	0.11
%define		plugin		keywordsuggestplugin
Summary:	Autocomplete feature for the keywords field.
Name:		trac-plugin-%{plugin}
Version:	%{trac_ver}.0.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
# Source0Download:	http://trac-hacks.org/changeset/latest/keywordsuggestplugin?old_path=/&filename=keywordsuggestplugin&format=zip
Source0:	%{plugin}.zip
# Source0-md5:	ee0297ad52e6abdc9be18e7def8fee8b
URL:		http://trac-hacks.org/wiki/KeywordSuggestPlugin
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{plugin}

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# warning: install_data: setup script did not provide a directory for 'COPYING'
# warning: install_data: setup script did not provide a directory for 'README'
#rm $RPM_BUILD_ROOT%{_prefix}/{COPYING,README}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	To enable the %{plugin} plugin, add to conf/trac.ini:

	[components]
	tracext.git.* = enabled
EOF
fi

%files
%defattr(644,root,root,755)
#%doc %{trac_ver}/README
#%dir %{py_sitescriptdir}/tracext
%{py_sitescriptdir}/keywordsuggest
%{py_sitescriptdir}/Trac*.egg-info
#%{py_sitescriptdir}/Trac*-nspkg.pth
