Name:           ros-indigo-visp-camera-calibration
Version:        0.8.1
Release:        0%{?dist}
Summary:        ROS visp_camera_calibration package

Group:          Development/Libraries
License:        GPLv2
URL:            http://wiki.ros.org/visp_camera_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-visp
Requires:       ros-indigo-visp-bridge
BuildRequires:  ros-indigo-camera-calibration-parsers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-visp
BuildRequires:  ros-indigo-visp-bridge

%description
visp_camera_calibration allows easy calibration of cameras using a customizable
pattern and ViSP library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 08 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.8.1-0
- Autogenerated by Bloom

* Tue Mar 31 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.8.0-0
- Autogenerated by Bloom

