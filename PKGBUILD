# Script generated with Bloom
pkgdesc="ROS - visp_hand2eye_calibration estimates the camera position with respect to its effector using the ViSP library."
url='http://wiki.ros.org/visp_hand2eye_calibration'

pkgname='ros-kinetic-visp-hand2eye-calibration'
pkgver='0.10.0_1'
pkgrel=1
arch=('any')
license=('GPLv2'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-proc'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-visp'
'ros-kinetic-visp-bridge'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-image-proc'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-visp'
'ros-kinetic-visp-bridge'
)

conflicts=()
replaces=()

_dir=visp_hand2eye_calibration
source=()
md5sums=()

prepare() {
    cp -R $startdir/visp_hand2eye_calibration $srcdir/visp_hand2eye_calibration
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

