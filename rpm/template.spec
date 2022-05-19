%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ros2-controllers-test-nodes
Version:        2.5.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers_test_nodes package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-rclpy
Requires:       ros-humble-std-msgs
Requires:       ros-humble-trajectory-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Demo nodes for showing and testing functionalities of the ros2_control
framework.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu May 19 2022 Denis Štogl <denis@stoglrobotics.de> - 2.5.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Denis Štogl <denis@stoglrobotics.de> - 2.2.0-2
- Autogenerated by Bloom

* Fri Mar 25 2022 Denis Štogl <denis@stoglrobotics.de> - 2.2.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Denis Štogl <denis@stoglrobotics.de> - 2.1.0-1
- Autogenerated by Bloom

