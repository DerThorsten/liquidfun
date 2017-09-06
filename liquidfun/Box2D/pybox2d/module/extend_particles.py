from ._pybox2d import *
from .tools import _classExtender


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

class ParticleFlag(object):
    waterParticle = 0
    # Removed after next simulation step.
    zombieParticle = 1 << 1
    # Zero velocity.
    wallParticle = 1 << 2
    # With restitution from stretching.
    springParticle = 1 << 3
    # With restitution from deformation.
    elasticParticle = 1 << 4
    # With viscosity.
    viscousParticle = 1 << 5
    # Without isotropic pressure.
    powderParticle = 1 << 6
    # With surface tension.
    tensileParticle = 1 << 7
    # Mix color between contacting particles.
    colorMixingParticle = 1 << 8
    # Call b2DestructionListener on destruction.
    destructionListenerParticle = 1 << 9
    # Prevents other particles from leaking.
    barrierParticle = 1 << 10
    # Less compressibility.
    staticPressureParticle = 1 << 11
    # Makes pairs or triads with other particles.
    reactiveParticle = 1 << 12
    # With high repulsive force.
    repulsiveParticle = 1 << 13
    # Call b2ContactListener when this particle is about to interact with
    # a rigid body or stops interacting with a rigid body.
    # This results in an expensive operation compared to using
    # fixtureContactFilterParticle to detect collisions between
    # particles.
    fixtureContactListenerParticle = 1 << 14
    # Call b2ContactListener when this particle is about to interact with
    # another particle or stops interacting with another particle.
    # This results in an expensive operation compared to using
    # particleContactFilterParticle to detect collisions between
    # particles.
    particleContactListenerParticle = 1 << 15
    # Call b2ContactFilter when this particle interacts with rigid bodies.
    fixtureContactFilterParticle = 1 << 16
    # Call b2ContactFilter when this particle interacts with other
    # particles.
    particleContactFilterParticle = 1 << 17

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
        d.shape = shape
    if stride is not None:
        d.stride = stride
    if particleCount is not None:
        d.particleCount = particleCount
    if group is not None:
        d.group(shape)
    
    return d



#class _ParticleSystem(b2ParticleSystem):
#    pass
#_classExtender(_ParticleSystem,['group','shape'])


class _ParticleGroupDef(b2ParticleGroupDef):

    @property
    def group(self):
        return self._group()
    @group.setter
    def group(self, group):
        self._setGroup(shape)


    @property
    def shape(self):
        return self._shape()
    @shape.setter
    def shape(self, shape):
        self._setShape(shape)

_classExtender(_ParticleGroupDef,['group','shape'])

