Name:           ros-hydro-visp-auto-tracker
Version:        0.8.1
Release:        0%{?dist}
Summary:        ROS visp_auto_tracker package

Group:          Development/Libraries
License:        GPLv2
URL:            http://wiki.ros.org/visp_auto_tracker
Source0:        %{name}-%{version}.tar.gz

Requires:       libdmtx-devel
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-resource-retriever
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-visp
Requires:       ros-hydro-visp-bridge
Requires:       ros-hydro-visp-tracker
Requires:       zbar-devel
BuildRequires:  libdmtx-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-resource-retriever
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-visp
BuildRequires:  ros-hydro-visp-bridge
BuildRequires:  ros-hydro-visp-tracker
BuildRequires:  zbar-devel

%description
Online automated pattern-based object tracker relying on visual servoing.
visp_auto_tracker wraps model-based trackers provided by ViSP visual servoing
library into a ROS package. The tracked object should have a QRcode of Flash
code pattern. Based on the pattern, the object is automaticaly detected. The
detection allows then to initialise the model-based trackers. When lost of
tracking achieves a new detection is performed that will be used to re-
initialize the tracker. This computer vision algorithm computes the pose (i.e.
position and orientation) of an object in an image. It is fast enough to allow
object online tracking using a camera.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Apr 08 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.8.1-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.8.0-0
- Autogenerated by Bloom

* Fri Aug 01 2014 Fabien Spindler <Fabien.Spindler@inria.fr> - 0.7.5-0
- Autogenerated by Bloom

