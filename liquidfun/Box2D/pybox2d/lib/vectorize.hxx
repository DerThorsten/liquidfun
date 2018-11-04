#pragma once

#include <Box2D/Box2D.h>

#include "holder.hxx"
#include <vector>

namespace py = pybind11;




class BodyVector : public std::vector<b2Body * >
{
};
class BodySet : public std::set<b2Body * >
{
};


class JointVector : public std::vector<b2Joint * >
{
};
class JointSet : public std::set<b2Joint * >
{
};


class FixtureVector : public std::vector<b2Fixture * >
{
};
class FixtureSet : public std::set<b2Fixture * >
{
};