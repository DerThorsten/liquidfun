#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <Box2D/Box2D.h>


// struct b2ContactProxy{
//     b2ContactProxy(b2Contact * contact)
//     :   contact_(contact){ 
//     }
//     b2Contact * contact_;

//     b2Fixture * GetFixtureA(){
//         return contact_->GetFixtureA();
//     }
//     b2Fixture * GetFixtureB(){
//         return contact_->GetFixtureB();
//     }
//     void  GetWorldManifold(b2WorldManifold* worldManifold)const{
//         contact_->GetWorldManifold(worldManifold);
//     }
// };


// struct b2ManifoldProxy{
//     b2ManifoldProxy(const b2Manifold * manifold)
//     : manifold_(manifold){

//     }

//     const b2Manifold * manifold_;
// };


// struct b2ContactImpulseProxy{
//     b2ContactImpulseProxy(const b2ContactImpulse * impulse)
//     : impulse_(impulse){

//     }

//     const b2ContactImpulse * impulse_;
// };