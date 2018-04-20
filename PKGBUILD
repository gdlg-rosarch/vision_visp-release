# Script generated with Bloom
pkgdesc="ROS - Converts between ROS structures and ViSP structures."
url='http://wiki.ros.org/visp_bridge'

pkgname='ros-lunar-visp-bridge'
pkgver='0.10.0_2'
pkgrel=1
arch=('any')
license=('GPLv2'
)

makedepends=('ros-lunar-camera-calibration-parsers'
'ros-lunar-catkin'
'ros-lunar-geometry-msgs'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-visp'
)

depends=('ros-lunar-camera-calibration-parsers'
'ros-lunar-geometry-msgs'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-visp'
)

conflicts=()
replaces=()

_dir=visp_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/visp_bridge $srcdir/visp_bridge
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

