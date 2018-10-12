%global pname   tvguideng

Name:           vdr-%{pname}
Version:        0.3.0
Release:        9%{?dist}
Summary:        TvGuideNG is a highly customizable 2D EPG viewer plugin
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://projects.vdr-developer.org/projects/plg-tvguideng
Source0:        https://projects.vdr-developer.org/git/vdr-plugin-tvguideng.git/snapshot/vdr-plugin-%{pname}-%{version}.tar.bz2
# https://projects.vdr-developer.org/issues/2427
Patch0:         %{pname}-gcc6.patch
# https://www.vdr-portal.de/index.php?attachment/41876-tvguideng-235-diff/
Patch1:         tvguideng_235.diff

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.0.0
BuildRequires:  libskindesignerapi-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       vdr-skindesigner >= 0.4.0
Requires:       vdr-epgsearch

%description 
"TvGuideNG" is a highly customizable 2D EPG viewer plugin.
The "Search & Recordings" Menue provided by the red button allows to search
in the EPG and manage timers, search timers, series timers and switch
timers in an convenient way.

%prep
%setup -qn vdr-plugin-%{pname}-%{version}
%patch0 -p1
%patch1 -p1

# std::auto_ptr deprecation warning in libstdc++ 5.1
sed -i -e 's|      std::auto_ptr|       std::unique_ptr|g' services/epgsearch.h

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY* README*
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-9
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.3.0-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-6
- Rebuilt for vdr-2.4.0
- Add tvguideng_235.diff

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-2
- Added %%{pname}-gcc6.patch

* Mon Mar 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sun Jan 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Wed Jan 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Fri Jun 26 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri May 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Sun Apr 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2
- added BR libskindesignerapi-devel

* Fri Mar 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.3-1
- Update to 0.0.3

* Sat Mar 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.2-1
- Update to 0.0.2
- corrected typo in %%description

* Fri Mar 13 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-1
- initial build

