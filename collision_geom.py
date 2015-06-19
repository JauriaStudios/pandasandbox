import itertools

from panda3d.core import NodePath
from panda3d.core import TransformState
from panda3d.core import Vec3

from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletConeShape
from panda3d.bullet import BulletConvexHullShape
from panda3d.bullet import BulletCylinderShape
from panda3d.bullet import BulletSphereShape
from panda3d.bullet import BulletTriangleMesh
from panda3d.bullet import BulletTriangleMeshShape

class Entity():
	@staticmethod
	def calcSize(model):
		entityModel = loader.loadModel(model)
		return Entity.calcNodeSize(entityModel)
	
	@staticmethod
	def calcNodeSize(node):
		bottomLeft, topRight = node.getTightBounds()
		width = topRight.x - bottomLeft.x
		depth = topRight.y - bottomLeft.y
		height = topRight.z - bottomLeft.z
		return Vec3(width, depth, height)
	
	@staticmethod
	def calcTransform(nodePath, root):
		bottomLeft, topRight = nodePath.getTightBounds()
		shapeOrigin = (bottomLeft + topRight)/2
		originOffset = shapeOrigin - nodePath.getPos()
		if root is None:
			# We only needed to calculate the shape offset
			return TransformState.makePos(originOffset)
		else:
			# Combine the shape offset with nodePath's transform to the root node
			transform = nodePath.getTransform(root)
			return transform.setPos(transform.getPos() + originOffset)
	
	@staticmethod
	def calcCollisionShape(shape, model):
		
		if shape == "geometry":
			return Entity.calcCollisionGeometryShapes(model)
		
		modelNode = loader.loadModel(model)
		modelNode
		shapes = []
		i = 0
		for child in modelNode.findAllMatches('**/+GeomNode'):
			
			shapes.append(Entity.calcNodeCollisionShape(shape, child, None))
			i += 1
		return shapes
	
	@staticmethod
	def calcNodeCollisionShape(shape, nodePath, root):
		width, depth, height = Entity.calcNodeSize(nodePath)
		transform = Entity.calcTransform(nodePath, root)
		if shape == "box":
			return [(BulletBoxShape(Vec3(width/2, depth/2, height/2)), transform)]
		elif shape == "sphere":
			return [(BulletSphereShape(width/2), transform)]
		elif shape == "cylinder":
			return [(BulletCylinderShape(width/2, height, 2), transform)]
		elif shape == "cone":
			return [(BulletConeShape(width/2, height), transform)]
		elif shape == "hull":
			geom = nodePath.node().getGeom(0)
			hull = BulletConvexHullShape()
			hull.addGeom(geom)
			return [(hull, TransformState.makeIdentity())]
		elif shape == "mesh":
			geom = nodePath.node().getGeom(0)
			mesh = BulletTriangleMesh()
			mesh.addGeom(geom)
			return [(BulletTriangleMeshShape(mesh, dynamic=False), TransformState.makeIdentity())]
		else:
			raise AttributeError('Collision type ' + str(shape) + ' does not exist!')
	
	@staticmethod
	def calcCollisionGeometryShapes(model):
		root = loader.loadModel(model)
		root.ls()
		shapes = []
		# Find any collider geometry and transform it into a collision shape
		for shape in ["box", "sphere", "cylinder", "cone", "hull", "mesh"]:
			for child in root.findAllMatches('**/*'):
				shapes = itertools.chain(shapes, Entity.calcNodeCollisionShape(shape, NodePath(child), root))
				child.removeNode()
		
		return shapes
