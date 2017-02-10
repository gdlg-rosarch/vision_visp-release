Name:           ros-kinetic-visp-camera-calibration
Version:        0.10.0
Release:        0%{?dist}
Summary:        ROS visp_camera_calibration package

Group:          Development/Libraries
License:        GPLv2
URL:            http://wiki.ros.org/visp_camera_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-camera-calibration-parsers
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-visp
Requires:       ros-kinetic-visp-bridge
BuildRequires:  ros-kinetic-camera-calibration-parsers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-visp
BuildRequires:  ros-kinetic-visp-bridge

%description
visp_camera_calibration allows easy calibration of cameras using a customizable
pattern and ViSP library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Feb 10 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.10.0-0
- Autogenerated by Bloom

* Fri May 20 2016 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.9.3-0
- Autogenerated by Bloom

* Thu May 19 2016 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.9.2-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.9.1-0
- Autogenerated by Bloom

