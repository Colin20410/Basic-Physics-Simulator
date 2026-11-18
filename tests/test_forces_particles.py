from scripts.particle_like import ParticleLike; from scripts.forces import Force, NetForce


def test_particle():
    from scripts.particle_like import ParticleLike
    from scripts.vectors import Vector

    particle = ParticleLike(1,2,3,4)

    particle.boost(1,5,3)
    f = Force(particle, 1,0,0)

    assert particle.mass == 4
    assert particle.position == Vector("position" , 1,2,3)
    assert particle.velocity == Vector("velocity" , 1 , 5, 3)
    assert particle.force_list == [f]
    assert particle.net_force == NetForce(1,0,0)


def test_net_force(): 

    from scripts.particle_like import ParticleLike

    particle1 = ParticleLike(0,0,0,10)

    f1 = Force(particle1, 10, 0, 0)
    assert particle1.net_force == NetForce(10,0,0)

    f2 = Force(particle1, 0, 10,0)
    assert particle1.net_force == NetForce(10,10,0)

    assert particle1.force_list == [f1, f2]



