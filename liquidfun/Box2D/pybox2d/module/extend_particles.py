from pybox2d import *


class ParticleGroupFlag(object):
    # prevents overlapping or leaking.
    solidParticleGroup = 1 << 0
    # Keeps its shape.
    rigidParticleGroup = 1 << 1
    # Won't be destroyed if it gets empty.
    particleGroupCanBeEmpty = 1 << 2
    # Will be destroyed on next simulation step.
    particleGroupWillBeDestroyed = 1 << 3
    # Updates depth data on next simulation step.
    particleGroupNeedsUpdateDepth = 1 << 4
    particleGroupInternalMask = particleGroupWillBeDestroyed | particleGroupNeedsUpdateDepth






def particleSystemDef(
    strictContactCheck = False,
    density = 1.0,
    gravityScale = 1.0,
    radius = 1.0,
    maxCount = 0,
    pressureStrength = 0.05,
    dampingStrength = 1.0,
    elasticStrength = 0.25,
    springStrength = 0.25,
    viscousStrength = 0.25,
    surfaceTensionPressureStrength = 0.2,
    surfaceTensionNormalStrength = 0.2,
    repulsiveStrength = 1.0,
    powderStrength = 0.5,
    ejectionStrength = 0.5,
    staticPressureStrength = 0.2,
    staticPressureRelaxation = 0.2,
    staticPressureIterations = 8,
    colorMixingStrength = 0.5,
    destroyByAge = True,
    lifetimeGranularity = 1.0 / 60.0
):
    d = b2ParticleSystemDef()
    d.pressureStrength = pressureStrength
    d.dampingStrength = dampingStrength
    d.elasticStrength = elasticStrength
    d.springStrength = springStrength
    d.viscousStrength = viscousStrength
    d.surfaceTensionPressureStrength = surfaceTensionPressureStrength
    d.surfaceTensionNormalStrength = surfaceTensionNormalStrength
    d.repulsiveStrength = repulsiveStrength
    d.powderStrength = powderStrength
    d.ejectionStrength = ejectionStrength
    d.staticPressureStrength = staticPressureStrength
    d.staticPressureRelaxation = staticPressureRelaxation
    d.staticPressureIterations = staticPressureIterations
    d.colorMixingStrength = colorMixingStrength
    d.destroyByAge = destroyByAge
    d.lifetimeGranularity = lifetimeGranularity

    return d


def particleGroupDef(flags=None,groupFlags=None,position=None,
                     angle=None,linearVelocity=None,angularVelocity=None,
                     color=None,strength=None,shape=None,stride=None,
                     particleCount=None,group=None):
    
    d = b2ParticleGroupDef()

    if flags is not None:
        d.flags = flags
    if groupFlags is not None:
        d.groupFlags = groupFlags
    if position is not None:
        d.position = position
    if angle is not None:
        d.angle = angle
    if linearVelocity is not None:
        d.linearVelocity = linearVelocity
    if angularVelocity is not None:
        d.angularVelocity = angularVelocity
    if color is not None:
        d.color = color
    if linearVelocity is not None:
        d.linearVelocity = linearVelocity
    if angularVelocity is not None:
        d.angularVelocity = angularVelocity
    if color is not None:
        d.color = color
    if strength is not None:
        d.strength = strength
    if shape is not None:
        d.SetShape(shape)
    if stride is not None:
        d.stride = stride
    if particleCount is not None:
        d.particleCount = particleCount
    if group is not None:
        d.SetGroupr(shape)
    
    return d
