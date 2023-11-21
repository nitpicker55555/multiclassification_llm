const data = {
    'Autonomous Vehicles': {
        'Types': new Set(['autonomous vehicle', 'driverless cars', 'self-driving bus', 'autonomous vehicles', 'self-driving vehicle', 'self-driving Uber car', 'self-driving car', 'autonomous cars', 'self-driving trucks', 'autonomous trucks', 'self-driving cars']),
        'Technology': new Set(['driver assist technology', 'driver-assist systems', 'capability', 'technology', 'driver assistance systems', 'self-driving taxis', 'lidar sensors', 'robotaxis', 'Full Self-Driving', 'autopilot system', 'autonomous mode', 'software']),
        'Companies & Brands': new Set(['General Motors Co', 'Apple', 'Model X', 'Nvidia', 'General Motors', 'Alphabet Inc', 'Waymo', 'GM', 'Model 3', 'Google logo', 'Model S', 'Model Y', 'Google', 'Lyft', 'Uber', 'Toyota', 'Ford', 'Tesla Model 3', 'Tesla']),
        'Regulation & Safety': new Set(['Department of Motor Vehicles', 'safety', 'FSD', 'National Transportation Safety Board', 'Insurance Institute for Highway Safety', 'safety standardseatures', 'public safety'])
    }
};

function createTree(container, obj) {
    container.appendChild(buildTree(obj));
}

function buildTree(obj) {
    const ul = document.createElement('ul');
    for (const key in obj) {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(key));
        if (typeof obj[key] === 'object' && obj[key] !== null) {
            li.appendChild(buildTree(Array.from(obj[key])));
        }
        ul.appendChild(li);
    }
    return ul;
}

const treeContainer = document.getElementById('tree');
createTree(treeContainer, data);
