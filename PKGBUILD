# Script generated with Bloom
pkgdesc="ROS - Online automated pattern-based object tracker relying on visual servoing. visp_auto_tracker wraps model-based trackers provided by ViSP visual servoing library into a ROS package. The tracked object should have a QRcode of Flash code pattern. Based on the pattern, the object is automaticaly detected. The detection allows then to initialise the model-based trackers. When lost of tracking achieves a new detection is performed that will be used to re-initialize the tracker. This computer vision algorithm computes the pose (i.e. position and orientation) of an object in an image. It is fast enough to allow object online tracking using a camera."
url='http://wiki.ros.org/visp_auto_tracker'

pkgname='ros-kinetic-visp-auto-tracker'
pkgver='0.10.0_1'
pkgrel=1
arch=('any')
license=('GPLv2'
)

makedepends=('libdmtx'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-visp'
'ros-kinetic-visp-bridge'
'ros-kinetic-visp-tracker'
'zbar'
)

depends=('libdmtx'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-visp'
'ros-kinetic-visp-bridge'
'ros-kinetic-visp-tracker'
'zbar'
)

conflicts=()
replaces=()

_dir=visp_auto_tracker
source=()
md5sums=()

prepare() {
    cp -R $startdir/visp_auto_tracker $srcdir/visp_auto_tracker
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

