import numpy as np
from   wpimath.geometry import *
from   frc_apriltags.Utilities.AprilTagFieldLayout import AprilTagFieldLayout

field = AprilTagFieldLayout.fromJson("2023-chargedup", False)
print(field.getTagPose(7))

pose1 = Pose3d(
    Translation3d(0, 0, 0),
    Rotation3d(0, 0, np.pi*0)
)

# Gets things in the right direction
pose2 = Pose3d(
    Translation3d(1, 1, 0),
    Rotation3d(0, 0, 0)
)
trans1 = Transform3d(
    Translation3d(),
    Rotation3d(pose1.rotation().X(), pose1.rotation().Y(), pose1.rotation().Z())
)
pose2 = pose2.transformBy(trans1)

# 
trans2 = Transform3d(
    pose2.translation(),
    pose2.rotation()
)

print(pose1.transformBy(trans2).toPose2d())