Name:           ros-jade-visp-tracker
Version:        0.9.0
Release:        0%{?dist}
Summary:        ROS visp_tracker package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/wiki/visp_tracker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-proc
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-generation
Requires:       ros-jade-message-runtime
Requires:       ros-jade-nodelet
Requires:       ros-jade-resource-retriever
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-visp
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-proc
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-resource-retriever
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

%description
Wraps the ViSP moving edge tracker provided by the ViSP visual servoing library
into a ROS package. This computer vision algorithm computes the pose (i.e.
position and orientation) of an object in an image. It is fast enough to allow
object online tracking using a camera.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Dec 20 2015 Fabien Spindler <fabien.spindler@inria.fr> - 0.9.0-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Fabien Spindler <fabien.spindler@inria.fr> - 0.8.0-0
- Autogenerated by Bloom

