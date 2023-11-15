%global pname   tvguideng
# version we want build against
%global vdr_version 2.6.1
%if 0%{?fedora} >= 38
%global vdr_version 2.6.3
%endif

Name:           vdr-%{pname}
Version:        0.3.4
Release:        1%{?dist}
Summary:        TvGuideNG is a highly customizable 2D EPG viewer plugin
License:        GPLv2+
URL:            https://gitlab.com/kamel5/tvguideng
Source0:        https://gitlab.com/kamel5/tvguideng/-/archive/%{version}/%{pname}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
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
%autosetup -n %{pname}-%{version}

# std::auto_ptr deprecation warning in libstdc++ 5.1
sed -i -e 's|std::auto_ptr|std::unique_ptr|g' services/epgsearch.h

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY* README*
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Wed Nov 15 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Dec 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.3-8
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.3-7
- Rebuilt for new VDR API version

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Apr 11 2022 Sérgio Basto <sergio@serjux.com> - 0.3.3-5
- Rebuilt for VDR 2.6.1

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.3-4
- Rebuilt for new VDR API version

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.3-3
- Rebuilt for new VDR API version

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-5
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-4
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-3
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-12
- Rebuilt for new VDR API version 2.4.1

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-11
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

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

