using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour
{

    public float speed = 10;

    // Dirty flag for checking if movement was made or not
    public bool MovementDirty { get; set; }

    void Start()
    {
        MovementDirty = false;
    }

    void Update()
    {
        float translation = Input.GetAxis("Vertical");
        if (translation != 0)
        {
            transform.Translate(Vector3.up * Input.GetAxis("Vertical") * Time.deltaTime * speed);
            MovementDirty = true;
        }

        float rotation = Input.GetAxis("Horizontal");
        if (rotation != 0)
        {
            transform.Translate(Vector3.right * Input.GetAxis("Horizontal") * Time.deltaTime * speed);
            MovementDirty = true;
        }
    }
}



