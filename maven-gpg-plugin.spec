%global pkg_name maven-gpg-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.4
Release:        11.10%{?dist}
Summary:        Maven GPG Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-gpg-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
Patch0:         0001-Add-support-for-maven-3.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix_java_common}ant
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-install-plugin
BuildRequires: %{?scl_prefix}maven-compiler-plugin
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-surefire-plugin
BuildRequires: %{?scl_prefix}maven-jar-plugin
BuildRequires: %{?scl_prefix}maven-javadoc-plugin

# Uses system gpg binary for actual signing
Requires:      gnupg


%description
This plugin signs all of the project's attached artifacts with
GnuPG. It adds goals gpg:sign and gpg:sign-and-deploy-file.


%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x

# migrate to maven 3.x 
%patch0 -p1
sed -i 's/${mavenVersion}/3.0.4/' pom.xml
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4-11.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4-11.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-11
- Mass rebuild 2013-12-27

* Wed Jul 17 2013 Tomas Radej <tradej@redhat.com> - 1.4-10
- Added R on gnupg (used for actual singing)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Jun 25 2013 Tomas Radej <tradej@redhat.com> - 1.4-8
- Removed BR on ant-nodeps (no longer available)

* Tue Feb 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7
- Use default packaging layout

* Tue Feb 12 2013 Michal Srb <msrb@redhat.com> - 1.4-6
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Install LICENSE and NOTICE files (#879367)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-1
- Update to latest upstream version.

* Mon Jun 13 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Update to latest upstream version

* Fri Mar 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-1
- Update to new upstream release.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun  2 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-2
- Fix depmap call
- Add gnupg2 to Requires

* Tue Jun  1 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-1
- Initial package
