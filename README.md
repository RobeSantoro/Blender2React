# Blender 2 React

This Blender Addon is a learning project. It started as an ambitious project to generate react-three-fiber and Drei components from a Blender scene, but it is still a messy work in progress.

I created it during the development of [this animated scrolling home page](https://github.com/RobeSantoro/publifest-3d-r3f) for a client. I wanted to create some tools to automate tedious tasks and to learn more about Blender API and react-three-fiber, focusing on Drei components.

## Installation

Clone the repository to your Blender addons folder or download the zip and install it from the Blender preferences.

## Usage / Status

- **Save the Blender scene**.  

### **Initialization**

- [x] Set the root path where you want the react-three-fiber project to be created.
- [x] Set the name of the react-three-fiber project.

> Note: *The project name will be used as the name of the react-three-fiber project. If you not specify a name, "r3f-project" will be used, and the project will be created next to the Blender scene.*

- [x] Set the absolute path of the public folder where to export

- [x] **Init**

- [x] **Start Dev Server**

- [x] **Open Project in VSCode**

- [x] **Open Project in Explorer**

### **TODO**

- [ ] Create a Component Structure to hold the exported react-three-fiber components. (Suspense, Canvas, Lights, Camera, etc.)

- [x] Manage the Camera Export to glb.

> I found a way to attach the default camera of the `<Canvas>` in a useFrame in the following way, by animating two eEmpties in the blender scene.  
>  
> The first one represent the camera position and is the parent of the actual camera which has a Track To modifier the point to the second empty, which represent the camera aim.

#### **Blender Camera Hierarchy**

![Camera Hierarchy](img/camera-hierarchy.jpg)

#### **Camera Component**

```jsx
import { useEffect } from 'react'
import { useFrame } from '@react-three/fiber'
import { useScroll, useGLTF, useAnimations } from '@react-three/drei'

export default function Camera(props) {

    const scrollData = useScroll()
    
    const { scene, nodes, animations } = useGLTF('/camera-transformed.glb')
    const { actions } = useAnimations(animations, scene)
    
    useEffect(() => void (actions['camera'].time = 0), [actions])
    useFrame(({ mouse, camera }) => {

        // Get the camera nulls
        const camera_null = nodes['Camera_Pos'].position
        const camera_aim_null = nodes['Camera_Aim'].position

        camera.position.x = camera_null.x
        camera.position.y = camera_null.y
        camera.position.z = camera_null.z

        camera.lookAt(...camera_aim_null)

        const action = actions['camera']
        action.time = scrollData.offset * props.multiplier
    })

    useEffect(() => void (actions['camera'].play().paused = true), [actions])

    return <primitive object={scene} props />
}

useGLTF.preload('/camera-transformed.glb')
```

> Note that in the props I'm passing a multiplier to the camera component, to control the speed of the animation based on the actual scroll.

- [ ] Create a react-three-fiber component for each Collection.

- [ ] Create a react-three-fiber component for selected Collection.

- [ ] Add a useScroll hook to the exported component.

### **Utilities**

- [x] **Push Down Selected**: Push-down the action of the selected object to its NLA track.

- [x] **Rename Tracks**: Rename the tracks of the active collection to match the name of the collection itself.

- [x] **Rename Geometry**: Rename the geometry of the selected object using the `object name` + `_geo` suffix.

### **Export**

> At the moment you can Work on the animation in the blender scene, and set up the react-three-fiber project as you want*. The export will export the NLA track to the R3F Export Path (public folder)

- [x] **Export All**: Export all the Collections to .glb files and ~~react-three-fiber components~~.

- [x] **Export Active**: Export the Active Collection to a .glb file and ~~a react-three-fiber component~~.
