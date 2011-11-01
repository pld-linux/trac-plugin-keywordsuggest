%define		trac_ver	0.11
%define		plugin		keywordsuggest
Summary:	Autocomplete feature for the keywords field
Name:		trac-plugin-%{plugin}
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/keywordsuggestplugin?old_path=/&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	2196205c125b97ae1767db44ef5d74f3
URL:		http://trac-hacks.org/wiki/KeywordSuggestPlugin
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KeywordsSuggestPlugin provides an autocomplete function for the
keywords ticket field. Optionally, it is possible to restrict the list
of allowed keywords.

The KeywordSuggestPlugin uses the jQuery plugin: Autocomplete for the
javascript part.

%prep
%setup -qc
mv %{plugin}plugin/%{trac_ver}/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin "keywordsuggest.keywordsuggest.*"

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/keywordsuggest
%{py_sitescriptdir}/TracKeywordSuggest-*.egg-info
