%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2-controllers-test-nodes
Version:        4.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers_test_nodes package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rclpy
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-trajectory-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%description
Demo nodes for showing and testing functionalities of the ros2_control
framework.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Dec 12 2023 Denis Štogl <denis@stoglrobotics.de> - 4.2.0-1
- Autogenerated by Bloom

* Fri Dec 01 2023 Denis Štogl <denis@stoglrobotics.de> - 4.1.0-1
- Autogenerated by Bloom

* Tue Nov 21 2023 Denis Štogl <denis@stoglrobotics.de> - 4.0.0-1
- Autogenerated by Bloom

* Tue Oct 31 2023 Denis Štogl <denis@stoglrobotics.de> - 3.17.0-1
- Autogenerated by Bloom

* Wed Sep 20 2023 Denis Štogl <denis@stoglrobotics.de> - 3.16.0-1
- Autogenerated by Bloom

* Tue Sep 12 2023 Denis Štogl <denis@stoglrobotics.de> - 3.15.0-1
- Autogenerated by Bloom

* Wed Aug 16 2023 Denis Štogl <denis@stoglrobotics.de> - 3.14.0-1
- Autogenerated by Bloom

* Fri Aug 04 2023 Denis Štogl <denis@stoglrobotics.de> - 3.13.0-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Denis Štogl <denis@stoglrobotics.de> - 3.12.0-1
- Autogenerated by Bloom

* Sat Jun 24 2023 Denis Štogl <denis@stoglrobotics.de> - 3.11.0-1
- Autogenerated by Bloom

* Tue Jun 06 2023 Denis Štogl <denis@stoglrobotics.de> - 3.10.1-1
- Autogenerated by Bloom

* Sun Jun 04 2023 Denis Štogl <denis@stoglrobotics.de> - 3.10.0-1
- Autogenerated by Bloom

* Sun May 28 2023 Denis Štogl <denis@stoglrobotics.de> - 3.9.0-1
- Autogenerated by Bloom

* Sun May 14 2023 Denis Štogl <denis@stoglrobotics.de> - 3.8.0-1
- Autogenerated by Bloom

* Tue May 02 2023 Denis Štogl <denis@stoglrobotics.de> - 3.7.0-1
- Autogenerated by Bloom

* Sat Apr 29 2023 Denis Štogl <denis@stoglrobotics.de> - 3.6.0-1
- Autogenerated by Bloom

* Fri Apr 14 2023 Denis Štogl <denis@stoglrobotics.de> - 3.5.0-1
- Autogenerated by Bloom

* Sun Apr 02 2023 Denis Štogl <denis@stoglrobotics.de> - 3.4.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Denis Štogl <denis@stoglrobotics.de> - 3.3.0-2
- Autogenerated by Bloom

