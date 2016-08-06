/*
* Copyright (c) 2016 Thorsten Beier
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
* 1. The origin of this software must not be misrepresented; you must not
* claim that you wrote the original software. If you use this software
* in a product, an acknowledgment in the product documentation would be
* appreciated but is not required.
* 2. Altered source versions must be plainly marked as such, and must not be
* misrepresented as being the original software.
* 3. This notice may not be removed or altered from any source distribution.
*/

#ifndef B2_EXTENSION_MULTI_GRAVITY_WORLD_HXX
#define B2_EXTENSION_MULTI_GRAVITY_WORLD_HXX

#include <Box2D/Dynamics/b2World.h>





struct b2GravitySourceDef{


    enum b2GravitySourceType{
        e_point = 0,
        e_shape = 1,
        e_unknown =3
    };



    b2GravitySourceDef(){
        sourceType = b2GravitySourceType::e_point;
        gravityFiter = b2GravityFilter;
    }

    b2GravitySourceType sourceType;
    b2GravityFilter gravityFiter;
};




struct b2PointGravitySourceDef : public b2GravitySourceDef{
    b2PointGravitySourceDef(){
        this->sourceType = b2GravitySourceType::e_point;
        this->source = b2Vec2(0,0);
        this->decay = 2;
        this->mass = 1.0;
        this->truncationDistance = -1.0;
    }
    b2Vec2 source;
    float32 decay;
    float32 mass;
    float32 truncationDistance;
};






class b2GravitySource{
public:

    virtual ~b2GravitySource(){}

    b2GravitySource(const b2GravitySourceDef * def){

    }
    

    virtual  void ApplyForce(const b2Vec2 & centerOfMass, const b2Body * body) const = 0;

private:    

};


class b2PointGravitySource : public b2GravitySource{
public:

    virtual ~b2PointGravitySource(){}

    b2PointGravitySource(const b2PointGravitySourceDef * def)
    : b2GravitySource(def){

    }
    
    
    // apply the actual force to the center of mass
    virtual  void ApplyForce(const b2Vec2 & centerOfMass, const b2Body * body) const {

    }

private:    

};


class b2MultiGravityWorld : public b2World{
public:
    b2MultiGravityWorld(const b2Vec2 & gravity )
    :   b2World(gravity){

    }

    ~ b2MultiGravityWorld(){
        for(size_t i=0; i< gravitySources_.size(); ++i){
            delete gravitySources_[i];
        }

    }

    b2GravitySource * CreateGravitySource(const  b2GravitySourceDef  * def){
        b2GravitySource * gs = NULL;
        if(def->sourceType == b2GravitySourceDef::e_point){
            gs = new b2PointGravitySource(static_cast<const b2PointGravitySourceDef *>(def));
        }

        //GravitySource * gs = new GravitySource(def);
        gravitySources_.push_back(gs);
        return gs;
    }
    void Step(  float32 timeStep,
                int32 velocityIterations,
                int32 positionIterations,
                int32 particleIterations){

        if(!gravitySources_.empty()){
            // naively apply on all bodies
            b2Body * currentBody = this->GetBodyList();
            while(currentBody != NULL){

                if(currentBody->GetType() == b2_dynamicBody){
                    const b2Vec2 & centerOfMass = currentBody->centerOfMass();
                }
                // get next
                currentBody = currentBody ->GetNext();
            }
        }


        b2World::Step(timeStep, velocityIterations, positionIterations, particleIterations);
    }

private:
    std::vector<b2GravitySource *> gravitySources_;

};

#endif // B2_EXTENSION_MULTI_GRAVITY_WORLD_HXX
