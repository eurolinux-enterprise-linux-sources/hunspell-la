Name: hunspell-la
Summary: Latin hunspell dictionaries
%define upstreamid 20110807
Version: 0.%{upstreamid}
Release: 5%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/e-files/1141/2/dict-la_2011-08-07.oxt
URL: http://extensions.services.openoffice.org/project/dict-la
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ and LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Latin hunspell dictionaries.

%prep
%setup -q -c -n hunspell-la

%build
for i in README_extension_owner-la.txt la/README_la.txt la/COPYING*; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p la/la.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/la.dic
cp -p la/la.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/la.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_extension_owner-la.txt la/README_la.txt la/COPYING_*
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110807-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Caolán McNamara <caolanm@redhat.com> - 0.20110807-4
- included (but unused) hyphenation patterns are under unversioned LGPL

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110807-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110807-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110807-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100823-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100823-1
- latest version

* Fri Jul 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20080903-5
- drop build require

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080903-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20080903-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080903-1
- initial version
