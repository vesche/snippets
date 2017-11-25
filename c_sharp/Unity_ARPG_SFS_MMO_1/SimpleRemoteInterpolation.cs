using UnityEngine;
using System.Collections;

/**
 * Extremely simple and dumb interpolation script.
 * But it works for this example.
 */
public class SimpleRemoteInterpolation : MonoBehaviour
{
    private Vector3 desiredPos;

    private float dampingFactor = 5f;

    void Start()
    {
        desiredPos = this.transform.position;
    }

    public void SetTransform(Vector3 pos, bool interpolate)
    {
        // If interpolation, then set the desired pososition+rotation; else force set (for spawning new models)
        if (interpolate)
        {
            desiredPos = pos;
        }
        else
        {
            this.transform.position = pos;
        }
    }

    void Update()
    {
        this.transform.position = Vector3.Lerp(transform.position, desiredPos, Time.deltaTime * dampingFactor);
    }
}
