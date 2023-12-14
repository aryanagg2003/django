const APP_ID = 'a4a28c18dfd1484395e02aa118be8855'
const CHANNEL = 'main'
const TOKEN = '007eJxTYGAL1j6Z8VRwyuf1v5kS7+WvyLBeEOdwIOLhjXyxkG3dIX4KDIkmiUYWyYYWKWkphiYWJsaWpqkGRomJhoYWSakWFqamyu/LUxsCGRm4NtgyMTJAIIjPwpCbmJnHwAAAOiYeqw=='

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `
        <div class="video-container" id="user-container-${UID}">
            <div class="username-wrapper"><span id="user-name">My Name</span></div>
            <div class="video-player" id="user-${UID}"></div>
        </div>
    `
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])

}

joinAndDisplayLocalStream()