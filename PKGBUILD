# Script generated with Bloom
pkgdesc="ROS - Virtual package providing ViSP related packages."
url='http://wiki.ros.org/vision_visp'

pkgname='ros-lunar-vision-visp'
pkgver='0.10.0_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-visp-auto-tracker'
'ros-lunar-visp-bridge'
'ros-lunar-visp-camera-calibration'
'ros-lunar-visp-hand2eye-calibration'
'ros-lunar-visp-tracker'
)

conflicts=()
replaces=()

_dir=vision_visp
source=()
md5sums=()

prepare() {
    cp -R $startdir/vision_visp $srcdir/vision_visp
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

