using UnityEngine;
using System.Collections;

public class CameraController : MonoBehaviour {

    private float speed = 10;
    public Transform target;
    //int degrees = 10;
    //int dragSpeed = 10;

    public float speedH = 2.0f;
    public float speedV = 2.0f;

    private float yaw = 0.0f;
    private float pitch = 0.0f;


    void Update()
    {
        if(!Input.GetMouseButton(1))
        {
            if (Input.GetKey(KeyCode.D))
            {
                transform.Translate(new Vector3(speed * Time.deltaTime, 0, 0));
            }
            if (Input.GetKey(KeyCode.A))
            {
                transform.Translate(new Vector3(-speed * Time.deltaTime, 0, 0));
            }
            if (Input.GetKey(KeyCode.W))
            {
                transform.Translate(new Vector3(0, 0, speed * Time.deltaTime));
            }
            if (Input.GetKey(KeyCode.S))
            {
                transform.Translate(new Vector3(0, 0, -speed * Time.deltaTime));
            }
        }

        if (Input.GetMouseButton(1))
        {

            yaw += speedH * Input.GetAxis("Mouse X");
            pitch -= speedV * Input.GetAxis("Mouse Y");

            transform.eulerAngles = new Vector3(pitch, yaw, 0.0f);
        }
    }
}


