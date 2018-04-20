# Script generated with Bloom
pkgdesc="ROS - Wraps the ViSP moving edge tracker provided by the ViSP visual servoing library into a ROS package. This computer vision algorithm computes the pose (i.e. position and orientation) of an object in an image. It is fast enough to allow object online tracking using a camera."
url='http://wiki.ros.org/wiki/visp_tracker'

pkgname='ros-kinetic-visp-tracker'
pkgver='0.10.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-proc'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-nodelet'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visp'
)

depends=('ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-proc'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-nodelet'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visp'
)

conflicts=()
replaces=()

_dir=visp_tracker
source=()
md5sums=()

prepare() {
    cp -R $startdir/visp_tracker $srcdir/visp_tracker
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

